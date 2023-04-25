from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Status:
    code: int

    @staticmethod
    def from_dict(obj: Any) -> "Status":
        assert isinstance(obj, dict)
        code = from_int(obj.get("code"))
        return Status(code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_int(self.code)
        return result


@dataclass
class GetData:
    status: Status
    excel_base64: str
    filename: str

    @staticmethod
    def from_dict(obj: Any) -> "GetData":
        assert isinstance(obj, dict)
        status = Status.from_dict(obj.get("status"))
        excel_base64 = from_str(obj.get("excelBase64"))
        filename = from_str(obj.get("filename"))
        return GetData(status, excel_base64, filename)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = to_class(Status, self.status)
        result["excelBase64"] = from_str(self.excel_base64)
        result["filename"] = from_str(self.filename)
        return result


def get_data_from_dict(s: Any) -> GetData:
    return GetData.from_dict(s)


def get_data_to_dict(x: GetData) -> Any:
    return to_class(GetData, x)
