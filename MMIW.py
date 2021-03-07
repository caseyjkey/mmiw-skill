import requests
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from datetime import datetime

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        handler_input.response_builder.speak("Welcome to MMIW ").set_should_end_session(False)
        return handler_input.response_builder.response    

class CatchAllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        print(exception)
        handler_input.response_builder.speak("Sorry, there was some problem. Please try again!!")
        return handler_input.response_builder.response

@sb.request_handler(can_handle_func=is_request_type("LaunchRequest"))
class LostInformationIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("LostInformationIntent")(handler_input)

    def handle(self, handler_input):
        name = handler_input.request_envelope.request.intent.slots['women'].value
        day = handler_input.request_envelope.request.intent.slots['day'].value
        #day = datetime.strptime(day, '%Y-%m-%d')
        url = "https://httpbin.org/post"
        #params = {"date": day}
        
        status = 200 # requests.post(url, data = params)
        
        speech_text = "My custom Intent handler " + status
        handler_input.response_builder.speak(speech_text).set_should_end_session(False)
        return handler_input.response_builder.response 

sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(LostInformationIntentHandler())
handler = sb.lambda_handler()

