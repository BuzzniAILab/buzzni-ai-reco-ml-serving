from buzzni.ai.reco.mlserving.webframeworks import WebFramework


class WebFrameworkFactory:

    @staticmethod
    def create(name: str, service_name: str) -> WebFramework:
        framework_creator = FRAMEWORKS.get(name)
        if framework_creator is None:
            raise NotImplementedError(f'Framework {name} is not implemented')

        return framework_creator(service_name)

    @staticmethod
    def _create_falcon(service_name: str):
        try:
            from .falcon import FalconFramework
            return FalconFramework(service_name=service_name)
        except ImportError:
            print('falcon >= 2 is required in order falcon as web-framework')


FRAMEWORKS = dict(
    falcon=WebFrameworkFactory._create_falcon
)
