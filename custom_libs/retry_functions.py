from requests import RequestException

def should_retry(exception):
    if isinstance(exception, RequestException):
        
        # connection error
        if exception.response is None:
            return True
        
        status = exception.response.status_code
        
        # only retries temporary errors
        return status in {500, 502, 503, 504, 408, 429}
    
    return False