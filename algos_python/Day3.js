/* 
    Given in an alumni interview in 2021.

    String Encode

    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 


    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
  */

    const str1 = "aaaabbcddd";
    const expected1 = "a4b2c1d3";

    const str2 = "";
    const expected2 = "";

    const str3 = "a";
    const expected3 = "a";

    const str4 = "bbcc";
    const expected4 = "bbcc";

    const str5 = "aaaabbcdddaaaa";
    const expected5 = "a8b2c1d3";
    const expected5_bonus = "a4b2c1d3a4";

/**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
*/
    function encodeStr(str) {
        var newStr = "";
        
        for (var i = 0; i < str.length; i++){
            var temp = str[0]
            if (str[i] != temp) {
                newStr += str[i]
                temp = str[i]
            }
            count = 0
            var j = i;
            while (temp = str[j]) {
                count += 1;
                j++
            }
        }
        return newStr;
    }

console.log(encodeStr(str1))

    /*****************************************************************************/

/* 
    String Decode  
*/

const str1a = "a3b2c1d3";
const expected1a = "aaabbcddd";

const str2b = "a3b2c12d10";
const expected2b = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {}

/*****************************************************************************/