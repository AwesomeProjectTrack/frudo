from src.output_formater.json_output_formater import JSONOutputFormater

output_formaters = {"json": JSONOutputFormater()}


def get_output_formater(name):
    return output_formaters.get(name)
