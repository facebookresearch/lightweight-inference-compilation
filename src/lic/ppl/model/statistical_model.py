# Copyright (c) Facebook, Inc. and its affiliates.
# This is a minimal subset of the beanmachine PPL necessary to demo LIC
import inspect
import warnings
from functools import wraps

from .rv_identifier import RVIdentifier
from ..world.world import world_context


class StatisticalModel(object):
    """
    Parent class to all statistical models.

    every random variable in the model needs to be defined with function
    declaration accompanied with @ppl.random_variable decorator.

    for instance, here is Gaussian Mixture Model implementation:


    K, alpha, beta, gamma = init()

    @ppl.random_variable
    def mu():
        return Normal(alpha, beta)

    @ppl.random_variable
    def z(i):
        return Uniform(K)

    @ppl.random_variable
    def y(i):
        return Normal(mu(z(i)), gamma)
    """

    @staticmethod
    def get_func_key(wrapper, arguments) -> RVIdentifier:
        """
        Creates a key to uniquely identify the Random Variable.

        :param wrapper: reference to the wrapper function
        :param arguments: function arguments

        :returns: tuple of function and arguments which is to be used to identify
        a particular function call.
        """
        return RVIdentifier(wrapper=wrapper, arguments=arguments)

    @staticmethod
    def sample(f):
        warnings.warn(
            "@sample will be deprecated, use @random_variable instead",
            DeprecationWarning,
        )
        return StatisticalModel.random_variable(f)

    @staticmethod
    def random_variable(f):
        """
        Decorator to be used for every stochastic random variable defined in
        all statistical models.
        """

        @wraps(f)
        def wrapper(*args):
            func_key = StatisticalModel.get_func_key(wrapper, args)
            world = world_context.get()
            if world:
                return world.update_graph(func_key)
            else:
                return func_key

        if inspect.ismethod(f):
            meth_name = f.__name__ + "_wrapper"
            setattr(f.__self__, meth_name, wrapper)
        else:
            f._wrapper = wrapper
        wrapper.is_random_variable = True
        return wrapper


random_variable = StatisticalModel.random_variable
