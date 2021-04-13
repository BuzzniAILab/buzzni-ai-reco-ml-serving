import falcon as f

from buzzni.ai.reco.mlserving.api import Request
from buzzni.ai.reco.mlserving.predictors import RESTPredictor
from buzzni.ai.reco.mlserving.predictors.runner import PredictorRunner


class InferenceResource:
    def __init__(self, predictor: RESTPredictor):
        self.predictor = predictor

    def on_post(self, req: f.Request, res: f.Response):
        mlserving_req = Request(req.media, req.headers)

        response = PredictorRunner.run_inference(self.predictor, mlserving_req)
        res.body = response.data
        res.status = response.status_string

        return res
