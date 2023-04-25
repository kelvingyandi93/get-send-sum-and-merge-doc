import requests
from Auth import auth_token
from getDatamodel import GetData


def get_data(dateFrom, dateTo, OCR):
    def getDataListBalance():
        url = "https://esignhub.docsol.id:8443/adimobile/billing/services/saldo/s/getBalanceMutationFile"

        bearer = auth_token()

        print(dateFrom, dateTo)

        headers = {
            "Authorization": f"Bearer {bearer}",
            "Content-Type": "application/json",
        }

        data = {
            "audit": {"callerId": "ADMCLIENT@CFI"},
            "tenantCode": "CFI",
            "balanceType": OCR,
            "referenceNo": "",
            "transactionType": None,
            "user": "",
            "officeCode": "",
            "processResult": "",
            "transactionDateStart": dateFrom,
            "transactionDateEnd": dateTo,
            "vendorCode": "ESG",
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            data = response.json()
            getData = GetData(data["status"], data["excelBase64"], data["filename"])
            return getData.excel_base64

        else:
            print("Error:", response.status_code)

    return getDataListBalance()
