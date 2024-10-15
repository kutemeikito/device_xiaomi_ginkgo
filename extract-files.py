#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
    libs_proto_3_9_1,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
namespace_imports = [
        "device/xiaomi/ginkgo",
        "hardware/qcom-caf/sm8150",
        "vendor/qcom/opensource/display",
        "hardware/qcom-caf/wlan",
        "vendor/qcom/opensource/dataservices",
]
lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/miwatermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
    ('vendor/lib64/libwvhidl.so', 'vendor/lib64/mediadrm/libwvdrmengine.so'): blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so')
        .add_needed('libcrypto_shim.so'),
    ('vendor/lib64/libvendor.goodix.hardware.biometrics.fingerprint@2.1.so', 'vendor/lib64/libgoodixhwfingerprint.so'): blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    
}  # fmt: skip

module = ExtractUtilsModule(
    'ginkgo',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()