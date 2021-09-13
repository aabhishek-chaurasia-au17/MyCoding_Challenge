class Account {
    constructor(number, balance, type) {
        this.type = type;
        this.number = number
        this.balance = balance
        this.withdrawLimit = undefined

        console.log(`
        Account Created Successfully. 
        Account Number : ${this.number}
        Type : ${this.type}
        Balance : ${this.balance}`)
    }

    deposit(amount) {
        this.balance += amount
        console.log(`
        ₹ ${amount} Deposited Successfully
        Current Balance : ₹ ${this.balance}`)
    }

    withdraw(amount) {
        if ((this.withdrawLimit == null) || (this.withdrawLimit > 0)) {
            if (amount > this.balance) {
                console.log(`
                Cannot Withdraw ₹ ${amount}, Insufficient Balance.
                Current Balance : ₹ ${this.balance}`)
            }
            else {
                this.balance -= amount
                console.log(`
                ₹ ${amount} Withdrawn Successfully
                Current Balance : ₹ ${this.balance}`)
                if (this.type =="Savings"){
                    this.withdrawLimit -= 1
                    console.log(`Withdrawals Left Today ${this.withdrawLimit}`) 
                }
            }
        }
        else {
            console.log("Unable to Withdraw, maximum Withdrawal Limit Reached for today!")
        }

    }
}


class Savings extends Account {
    constructor(number, balance) {
        super(number, balance, "Savings")
        this.withdrawLimit = 3
    }
}


class Current extends Account {
    constructor(number, balance) {
        super(number, balance, "Current")
        this.withdrawLimit = null
    }
}

const mySavings = new Savings(196900156, 1000)
mySavings.withdraw(100)
mySavings.withdraw(450)
mySavings.withdraw(1000)
mySavings.withdraw(10)
mySavings.withdraw(101)

const myCurrent = new Current(651009691, 2000)
myCurrent.deposit(100000)
myCurrent.withdraw(120)

