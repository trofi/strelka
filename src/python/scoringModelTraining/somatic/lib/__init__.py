#
# Strelka - Small Variant Caller
# Copyright (c) 2009-2016 Illumina, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

# coding=utf-8

import abc


class EVSModel(object):
    """ Base class for EVS models """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def train(self, tp, fp, columns, *args, **kwargs):
        """ Train model from sets of TPs and FPs

        :param tp: data frame with rows of TP instances.
        :type tp: pandas.DataFrame
        :param fp: data frame with rows of FP instances.
        :type fp: pandas.DataFrame
        :param columns: the feature columns to use

        """
        pass

    # noinspection PyUnusedLocal
    @abc.abstractmethod
    def classify(self, instances, columns, *args, **kwargs):
        """ Classify a set of instances after training

        :param instances: data frame with instances.
        :type instances: pandas.DataFrame
        :param columns: the feature columns to use

        :return: data frame with added column "tag" which gives the classification
        :rtype: pandas.DataFrame
        """
        instances["tag"] = "FP"
        return instances

    @abc.abstractmethod
    def save(self, filename):
        """ Save to file """
        pass

    @abc.abstractmethod
    def load(self, filename):
        """ Load from file """
        pass

    # model factory
    _models = {}

    @classmethod
    def register(cls, mname, mclass):
        cls._models[mname] = mclass

    @classmethod
    def create(cls, mname):
        return cls._models[mname]()

    @classmethod
    def names(cls):
        return cls._models.keys()


import strelka_rf   # noqa
import strelka_rf_indel   # noqa