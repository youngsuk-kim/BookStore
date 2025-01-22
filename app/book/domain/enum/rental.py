from enum import Enum


class RentalStatus(Enum):
    # 사용자가 책 렌탈을 요청한 상태.
    REQUESTED = 1,
    # 관리자의 승인을 대기하는 상태
    PENDING_APPROVAL = 2,
    # 관리자 승인 완료 상태
    APPROVED = 3,
    # 관리자 승인 거절 상태
    REJECTED = 4,
    # 대여 기간 초과 상태
    OVERDUE = 7,
    # 반납 요청 상태
    RETURN_REQUESTED = 8,
    # 반납 진행 중 상태
    RETURN_IN_PROGRESS = 9,
    # 반납 완료 상태
    RETURNED = 10,
    # 분실 상태
    LOST = 11,
    # 손상 상태
    DAMAGED = 12