# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2013, Numenta, Inc.  Unless you have an agreement
# with Numenta, Inc., for a separate license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

MODEL_PARAMS = {'aggregationInfo': {'days': 0,
                     'fields': [(u'dttm', 'first'), (u'value', 'sum')],
                     'hours': 1,
                     'microseconds': 0,
                     'milliseconds': 0,
                     'minutes': 0,
                     'months': 0,
                     'seconds': 0,
                     'weeks': 0,
                     'years': 0},
 'model': 'HTMPrediction',
 'modelParams': {'anomalyParams': {u'anomalyCacheRecords': None,
                                   u'autoDetectThreshold': None,
                                   u'autoDetectWaitRecords': None},
                 'clParams': {'alpha': 0.0923535690373405,
                              'regionName': 'SDRClassifierRegion',
                              'steps': '1',
                              'verbosity': 0},
                 'inferenceType': 'NontemporalMultiStep',
                 'sensorParams': {'encoders': {'_classifierInput': {'classifierOnly': True,
                                                                    'clipInput': True,
                                                                    'fieldname': 'value',
                                                                    'n': 521,
                                                                    'name': '_classifierInput',
                                                                    'type': 'AdaptiveScalarEncoder',
                                                                    'w': 21},
                                               u'dttm_dayOfWeek': None,
                                               u'dttm_timeOfDay': None,
                                               u'dttm_weekend': None,
                                               u'value': {'clipInput': True,
                                                          'fieldname': 'value',
                                                          'n': 443,
                                                          'name': 'value',
                                                          'type': 'AdaptiveScalarEncoder',
                                                          'w': 21}},
                                  'sensorAutoReset': None,
                                  'verbosity': 0},
                 'spEnable': True,
                 'spParams': {'boostStrength': 0.0,
                              'columnCount': 2048,
                              'globalInhibition': 1,
                              'inputWidth': 0,
                              'numActiveColumnsPerInhArea': 40,
                              'potentialPct': 0.8,
                              'seed': 1956,
                              'spVerbosity': 0,
                              'spatialImp': 'cpp',
                              'synPermActiveInc': 0.05,
                              'synPermConnected': 0.1,
                              'synPermInactiveDec': 0.0015515053077498862},
                 'tmEnable': True,
                 'tmParams': {'activationThreshold': 16,
                              'cellsPerColumn': 32,
                              'columnCount': 2048,
                              'globalDecay': 0.0,
                              'initialPerm': 0.21,
                              'inputWidth': 2048,
                              'maxAge': 0,
                              'maxSegmentsPerCell': 128,
                              'maxSynapsesPerSegment': 32,
                              'minThreshold': 12,
                              'newSynapseCount': 20,
                              'outputType': 'normal',
                              'pamLength': 5,
                              'permanenceDec': 0.1,
                              'permanenceInc': 0.1,
                              'seed': 1960,
                              'temporalImp': 'cpp',
                              'verbosity': 0},
                 'trainSPNetOnlyIfRequested': False},
 'predictAheadTime': None,
 'version': 1}