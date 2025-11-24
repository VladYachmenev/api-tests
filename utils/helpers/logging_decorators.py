import allure
import json
import time
from functools import wraps


def logging_api_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        response = func(*args, **kwargs)
        end_time = time.time()

        log_info = {
            'method': response.request.method,
            'url': response.request.url,
            'status_code': response.status_code,
            'time_ms': round((end_time - start_time) * 1000, 2)
        }
        if response.request.body:
            try:
                body = response.request.body
                if isinstance(body, bytes):
                    body = body.decode('utf-8')
                log_info['request_body'] = json.loads(body)
            except:
                log_info["request_body"] = str(response.request.body)

        try:
            if 'application/json' in response.headers.get('content-type', ''):
                log_info["response_body"] = response.json()
        except:
            pass

        allure.attach(
            json.dumps(log_info, indent=2, ensure_ascii=False),
            name=f"API Call: {func.__name__}",
            attachment_type=allure.attachment_type.JSON
        )

        return response
    return wrapper
