from falcon import Request, Response

from buzzni.ai.reco.mlserving.health import HealthHandler, HealthCheckRunner


class HealthResource:
    def __init__(self, health_handler: HealthHandler):
        self.health_handler = health_handler

    def on_get(self, _: Request, res: Response):
        health_resp = HealthCheckRunner.run(self.health_handler)

        res.status = health_resp.status_string
        res.body = health_resp.text
