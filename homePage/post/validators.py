from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # 파일 확장자 추출
    valid_extensions = ['.pdf', '.docx', '.xlsx', '.pptx', '.zip', '.hwp', '.png', '.jpg', '.jpeg', '.txt', ]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'지원되지 않는 파일 확장자입니다.')


def validate_file_size(value):
    filesize = value.size
    if filesize > 5242880:  # 5MB 제한
        raise ValidationError("최대 파일 크기는 5MB입니다.")
    elif filesize < 100:  # 최소 크기 제한 (예시)
        raise ValidationError("파일 크기가 너무 작습니다.")
