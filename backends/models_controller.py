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
    def get_model_by_slug_name(cls, model_name, **kwargs):
        model = cls.MODELS.get(model_name)
        if model is not None:
            instance = model(**kwargs)
            return instance

    @classmethod
    def all_parts_model(cls):
        return Wheel, Saddle, Frame, Chain, Fork, Brake

    @classmethod
    def get_model_for_creation(cls, model_name, request_dict):
        parameters_dict = {}
        for key, value in request_dict.iteritems():
            if key not in cls.MODELS.keys():
                return None
            if value is not None:
                model = cls.get_model_by_slug_name(key)
                model = model.get_by_id(value)
                if model is not None:
                    parameters_dict.update({key:(model,)})

        return cls.get_model_by_slug_name(model_name, **parameters_dict)

    @classmethod
    def get_model_for_update(cls, model_name, request_dict):
        import pdb; pdb.set_trace()
        parameters_dict = {}
        for key, value in request_dict.iteritems():
            if key not in cls.MODELS.keys():
                return None
            if value is not None:
                model = cls.get_model_by_slug_name(key)
                model = model.get_by_id(value)
                if model is not None:
                    parameters_dict.update({key:(model,)})

        return cls.get_model_by_slug_name(model_name, **parameters_dict)
