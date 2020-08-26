import pytest


@pytest.fixture(params=["AP", "BR", "EU", "KR", "LATAM", "NA"])
def region(request):
    return request.param


@pytest.fixture(
    params=[
        None,
        "ar-AE",
        "de-DE",
        "en-GB",
        "en-US",
        "es-ES",
        "es-MX",
        "fr-FR",
        "id-ID",
        "it-IT",
        "ja-JP",
        "ko-KR",
        "pl-PL",
        "pt-BR",
        "ru-RU",
        "th-TH",
        "tr-TR",
        "vi-VN",
        "zh-CN",
        "zh-TW",
    ]
)
def locale(request):
    return request.param

