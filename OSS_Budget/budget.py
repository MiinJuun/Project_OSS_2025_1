

import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.monthly_limit = 500000  

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

    def check_monthly_limit(self):
        today = datetime.date.today()
        current_year = today.year
        current_month = today.month

        monthly_total = sum(
            e.amount for e in self.expenses
            if datetime.date.fromisoformat(e.date).year == current_year and
               datetime.date.fromisoformat(e.date).month == current_month
        )

        print(f"\n[{current_year}년 {current_month}월 지출 점검]")
        print(f"이번 달 총 지출: {monthly_total}원")
        print(f"지출 한도: {self.monthly_limit}원")

        if monthly_total > self.monthly_limit:
            print("2025년 6월달 예산을 초과 하였습니다. \n")
        else:
            print("돈을 잘 아끼고 있습니다. 부자가 됩시다.\n")
