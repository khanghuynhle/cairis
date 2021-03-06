#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import sys
if (sys.version_info > (3,)):
  import http.client
  from http.client import BAD_REQUEST, CONFLICT, NOT_FOUND, OK
else:
  import httplib
  from httplib import BAD_REQUEST, CONFLICT, NOT_FOUND, OK
from flask_restful import fields
from flask import session, request, make_response
from flask_restful import Resource
from cairis.data.RiskLevelDAO import RiskLevelDAO
from cairis.tools.SessionValidator import get_session_id
from cairis.tools.JsonConverter import json_serialize

__author__ = 'Shamal Faily'


class RiskLevelAPI(Resource):

  def get(self, name):
    session_id = get_session_id(session, request)

    dao = RiskLevelDAO(session_id)
    riskLevel = dao.get_risk_level(name,'')
    dao.close()

    resp = make_response(json_serialize(riskLevel, session_id=session_id))
    resp.headers['Content-Type'] = "application/json"
    return resp
 

class RiskLevelByEnvironmentAPI(Resource):

  def get(self, name, environment):
    session_id = get_session_id(session, request)

    dao = RiskLevelDAO(session_id)
    riskLevel = dao.get_risk_level(name,environment)
    dao.close()

    resp = make_response(json_serialize(riskLevel, session_id=session_id))
    resp.headers['Content-Type'] = "application/json"
    return resp


class RiskThreatLevelAPI(Resource):

  def get(self,asset,threat):
    session_id = get_session_id(session, request)

    dao = RiskLevelDAO(session_id)
    riskLevel = dao.get_risk_threat_level(asset,threat,'')
    dao.close()

    resp = make_response(json_serialize(riskLevel, session_id=session_id))
    resp.headers['Content-Type'] = "application/json"
    return resp

class RiskThreatLevelByEnvironmentAPI(Resource):

  def get(self,asset,threat,environment):
    session_id = get_session_id(session, request)

    dao = RiskLevelDAO(session_id)
    riskLevel = dao.get_risk_threat_level(asset,threat,environment)
    dao.close()

    resp = make_response(json_serialize(riskLevel, session_id=session_id))
    resp.headers['Content-Type'] = "application/json"
    return resp
