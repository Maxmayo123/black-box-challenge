import sys
import math

def reimbursement(days, miles, receipts):
    log_receipts = math.log1p(receipts)  # log(1 + receipts)
    result = (
        -989.48
        + 47.80 * days
        + 0.42 * miles
        + 259.35 * log_receipts
    )
    return round(result, 2)

if __name__ == "__main__":
    days = float(sys.argv[1])
    miles = float(sys.argv[2])
    receipts = float(sys.argv[3])

    print(f"{reimbursement(days, miles, receipts):.2f}")
