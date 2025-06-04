import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def simple_tax_summary(self):
        try:
            income = int(input("총급여(원): "))
            tax_paid = int(input("올해 납부한 세금(원): "))
        except ValueError:
            print("숫자를 정확히 입력해주세요.\n")
            return

        
        money = sum(e.amount for e in self.expenses if e.category in ["의료", "기부"])
        tax_credit = int(money * 0.15)
        estimated_tax = int(income * 0.06)
        final_tax = max(estimated_tax - tax_credit, 0)

        print("\n[연말정산 결과]")
        print(f"공제 대상 합계: {money}원")
        print(f"세액 공제: {tax_credit}원")
        print(f"산출 세금: {final_tax}원")

        if tax_paid > final_tax:
            print(f"환급 예상: {tax_paid - final_tax}원\n")
        elif tax_paid < final_tax:
            print(f"추가 납부 예상: {final_tax - tax_paid}원\n")
        else:
            print("환급/추가 납부 없음\n")
