/* 
    Given an int to represent how much change is needed
    calculate the fewest number of coins needed to create that change,
    using the standard US denominations
*/
// quarter = 25 cents, dime = 10, nickel = 5, penny = 1
const cents1 = 25;
const expected1 = { quarter: 1 };

const cents2 = 50;
const expected2 = { quarter: 2 };

const cents3 = 9;
const expected3 = { nickel: 1, penny: 4 };

const cents4 = 99;
const expected4 = { quarter: 3, dime: 2, penny: 4 };

/**
 * Calculates the fewest coins of the standard American denominations needed
 *    to reach the given cents amount.
 * @param {number} cents
 * @returns {Object<string, number>} - A denomination table where the keys are
 *    denomination names and the value is the amount of that denomination
 *    needed.
 */

function fewestCoinChangeOld(cents) {
    const change = {};
    const quarters = Math.floor(cents / 25);
    cents -= quarters * 25;
    if (quarters > 0) {
        change["quarters"] = quarters;
    }

    const dimes = Math.floor(cents / 10);
    cents -= dimes * 10;
    if (dimes > 0) {
        change["dimes"] = dimes;
    }

    const nickels = Math.floor(cents / 5);
    cents -= nickels * 5;
    if (nickels > 0) {
        change["nickels"] = nickels;
    }

    if (cents > 0) {
        change["pennies"] = cents
    }
    return change
}


function fewestCoinChange(cents) {
    const values = {
        quarters: 25,
        dimes: 10,
        nickels: 5,
        pennies: 1
    };
    return Object.keys(values).reduce((acc, key) => {
        const coins = Math.floor(cents / values[key])
        cents %= values[key];
        if (coins > 0) {
            acc[key] = coins;
        }
        return acc;
    }, {});
}

console.log(fewestCoinChange(cents1)) // { quarter: 1 }
console.log(fewestCoinChange(cents2)) // { quarter: 2 }
console.log(fewestCoinChange(cents3)) // { nickel: 1, penny: 4 }
console.log(fewestCoinChange(cents4)) // { quarter: 3, dime: 2, penny: 4 }

