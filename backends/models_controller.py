from .bicycle_models import Wheel, Saddle, Frame, Chain, Fork, Brake, Bicycle


class ModelController:

    MODELS = {
        "wheel": Wheel,
        "wheels": Wheel,
        "saddle": Saddle,
        "frame": Frame,
        "chain": Chain,
        "fork": Fork,
        "brake": Brake,
        "bicycle": Bicycle
    }

    def __init__(self):
        pass

    @classmethod
    def get_instance_by_slug_name(cls, model_name, **kwargs):
        model = cls.MODELS.get(model_name)
        if model is not None:
            instance = model(**kwargs)
            return instance

    @classmethod
    def get_model_by_slug_name(cls, model_name):
        model = cls.MODELS.get(model_name)
        if model is not None:
            return model

    @classmethod
    def get_model_for_creation(cls, model_name, request_dict):
        params = cls.process_parameters_from_dict(request_dict)
        if params is not None:
            return cls.get_instance_by_slug_name(model_name, **params)
        return None

    @classmethod
    def process_parameters_from_dict(cls, request_dict):
        parameters_dict = {}
        for key, value in request_dict.iteritems():
            if key not in cls.MODELS.keys():
                return None
            if value is not None:
                model = cls.get_instance_by_slug_name(key)
                model = model.get_by_id(value)
                if model is not None:
                    parameters_dict.update({key:(model,)})
        if parameters_dict:
            return parameters_dict
        return None

    @classmethod
    def get_model_for_update(cls, id_model, model_name, request_dict):
        parameters = cls.process_parameters_from_dict(request_dict)
        model = cls.get_model_by_slug_name(model_name).get_by_id(id_model)

        for key, value in parameters.iteritems():
            setattr(model, key, value)
        return model
