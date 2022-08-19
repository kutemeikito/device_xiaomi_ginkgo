LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SRC_FILES := lib-imsvt.cpp
LOCAL_MODULE := lib-imsvt
LOCAL_MODULE_TAGS := optional

LOCAL_SRC_FILES := lib-watermarkshim.cpp
LOCAL_MODULE := lib-watermarkshim
LOCAL_MODULE_TAGS := optional
LOCAL_PROPRIETARY_MODULE := true

include $(BUILD_SHARED_LIBRARY)
