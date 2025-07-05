import datetime


def print_owing(invoice):
    outstanding = 0

    print("****************")
    print("*** 고객 채무 ***")
    print("****************")

    # 미해결 채무(outstanding)을 계산
    for o in invoice.orders:
        outstanding += o.amount

    # 마감일(dueDate) 기록
    today = datetime.date.today()
    invoice.due_date = today + datetime.timedelta(days=30)

    # 세부 사항 출력
    print(f"고객명: {invoice.customer}")
    print(f"채무액: {outstanding}")
    print(f"마감일: {invoice.due_date}")

def print_owing_refactored(invoice):
    print_banner("고객 채무")

    outstanding = calculate_outstanding(invoice)
    record_due_date(invoice)

    print_details(invoice, outstanding)

def print_banner(contents):
    print("****************")
    print(f"*** {contents} ***")
    print("****************")

def calculate_outstanding(invoice):
    ret = 0
    for o in invoice.orders:
        ret += o.amount
    return ret

def record_due_date(invoice):
    today = datetime.date.today()
    invoice.due_date = today + datetime.timedelta(days=30)

def print_details(invoice, outstanding):
    print(f"고객명: {invoice.customer}")
    print(f"채무액: {outstanding}")
    print(f"마감일: {invoice.due_date}")
