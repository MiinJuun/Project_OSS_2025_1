

import datetime
from expense import Expense, FixedExpense

class Budget:
    def __init__(self):
        self.expenses = []
        self.fixed_expenses = []
          

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

    def add_fixed_expense(self, category, description, amount):
        fixed = FixedExpense(category, description, amount)
        self.fixed_expenses.append(fixed)
        print("고정 지출이 추가되었습니다.\n")

    def list_fixed_expenses(self):
        if not self.fixed_expenses:
            print("고정 지출이 없습니다.\n")
            return
        print("\n[고정 지출 목록]")
        for idx, f in enumerate(self.fixed_expenses, 1):
            print(f"{idx}. {f}")
        print()

    def apply_fixed_expenses(self):
        today = datetime.date.today().isoformat()
        for f in self.fixed_expenses:
            expense = Expense(today, f.category, f.description, f.amount)
            self.expenses.append(expense)
        print("이번 달 고정 지출이 지출 내역에 반영되었습니다.\n")

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
            print("이번 달 예산을 초과했습니다.\n")
        else:
            print("예산을 넘지 않았습니다.\n")
