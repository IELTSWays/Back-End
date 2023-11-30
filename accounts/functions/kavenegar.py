from kavenegar import APIException, HTTPException, KavenegarAPI
from config.settings import KAVENEGAR_API_KEY, KAVENEGAR_TEMPLATE, KAVENEGAR_TEMPLATE_PASS


def send_sms_otp(phone_number: str, code: str) -> bool:
    api = KavenegarAPI(KAVENEGAR_API_KEY)
    params = {
        "receptor": phone_number,
        "template": KAVENEGAR_TEMPLATE,
        "token": code,
        "type": "sms",
    }
    try:
        api.verify_lookup(params)
        return True
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    except Exception as e:
        print(e)
    return True



def send_sms_pass(phone_number: str, link: str) -> bool:
    api = KavenegarAPI(KAVENEGAR_API_KEY)
    params = {
        "receptor": phone_number,
        "template": KAVENEGAR_TEMPLATE_PASS,
        "token": link,
        "type": "sms",
    }
    try:
        api.verify_lookup(params)
        return True
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    except Exception as e:
        print(e)
    return True



def send_sms_create_user(phone_number: str,name: str, username: str, password: str) -> bool:
    api = KavenegarAPI(KAVENEGAR_API_KEY)
    params = {
        "receptor": phone_number,
        "template": 'user-info',
        "token": name,
        "token2": username,
        "token3": password,
        "type": "sms",
    }
    try:
        api.verify_lookup(params)
        return True
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    except Exception as e:
        print(e)
    return True


def send_sms_create_staff(phone_number: str,name: str, username: str, password: str) -> bool:
    api = KavenegarAPI(KAVENEGAR_API_KEY)
    params = {
        "receptor": phone_number,
        "template": 'user-info-staff',
        "token": name,
        "token2": username,
        "token3": password,
        "type": "sms",
    }
    try:
        api.verify_lookup(params)
        return True
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    except Exception as e:
        print(e)
    return True




def send_sms_create_invoice(phone_number: str,name: str, invoice_id: str, id: str) -> bool:
    api = KavenegarAPI(KAVENEGAR_API_KEY)
    params = {
        "receptor": phone_number,
        "template": 'invoice',
        "token": name,
        "token2": invoice_id,
        "token3": str(id),
        "type": "sms",
    }
    try:
        api.verify_lookup(params)
        return True
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    except Exception as e:
        print(e)
    return True


