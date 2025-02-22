import db_connect 
import enable_log
import db_store
import api_requests

def main():
    enable_log
    db_connect
    db_store
    api_requests

if __name__ == '__main__':
    main()