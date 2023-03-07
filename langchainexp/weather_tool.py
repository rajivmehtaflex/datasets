# weather_tool.py
from langchain.agents import Tool
import re


def weather_data(where: str = None, when: str = None) -> str:
    '''
    mockup function: given a location and a time period,
    return weather forecast description in natural language (English)

    parameters:
        where: location
        when: time period

    returns:
        weather foreast description
    '''
    if where and when:
        return f'in {where}, {when} is sunny! Temperature is 20 degrees Celsius.'
    elif not where:
        return 'where?'
    elif not when:
        return 'when?'
    else:
        return 'I don\'t know'


def weather(when_and_where: str) -> str:
    '''
        input string where_and_when is a list of python string arguments
        with format as in the following example:

        "'arg 1' \"arg 2\" ... \"argN\""

        The weather function needs 2 arguments: where and when,
        so the when_and_where input string example could be:

        "'Genova, Italy' 'today'"
    '''

    # split the input string into a list of arguments
    pattern = r"(['\"])(.*?)\1"
    args = re.findall(pattern, when_and_where)
    args = [arg[1] for arg in args]

    # call the weather function passing arguments
    if args:
        where = args[0]
        when = args[1]
    else:
        where = when_and_where
        when = None

    result = weather_data(where, when)

    return result


Weather = Tool(
    name="weather",
    func=weather,
    description="helps to retrieve weather forecast, given arguments: 'where' (the location) and 'when' (the data or time period)"
)
