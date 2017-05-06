// @flow

/**
 * An ES6 written file that will be used as fixture to test the interaction
 * between the plugin and a flow server.
 *
 * A mistake was introduced line 16 causing a flow error line 18.
 */

type Price = number;
type Tax = number;

function applyTaxPrice(price: Price, tax: Tax) {
  return price * tax;
}

const priceBeforeTax = 23;
const tax = '0.20';

// [FAIL] This type is incompatible with the expected param type of number
const priceAfterTax: Price = applyTaxPrice(priceBeforeTax, tax)
