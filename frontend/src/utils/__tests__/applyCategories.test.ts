import {Product, Category} from "../../types";
import { applyCategories } from "../applyCategories";

describe('test applyCategories function', () => {
  it('should return an empty array', () => {
    const products: Product[] = [
      { id: 3, name: "test3", description: 'test3', price: 300, category: 'Электроника' },
    ];

    const categories: Category[] = ['Для дома'];
    expect(applyCategories(products, categories)).toEqual([]);
  });
});


const products: Product[] = [
  { id: 1, name: "test1", description: 'test1', price: 100, category: 'Одежда' },
  { id: 2, name: "test2", description: 'test2', price: 200, category: 'Для дома' },
  { id: 3, name: "test3", description: 'test3', price: 300, category: 'Электроника' },
];

const testCases = [
  {
    products: products,
    categories: [] as Category[],
    expectedProducts: products,
  },
  {
    products: products,
    categories: ['Одежда'] as Category[],
    expectedProducts: [products[0]],
  },
  {
    products: products,
    categories: ['Электроника'] as Category[],
    expectedProducts: [products[2]],
  },
  {
    products: products,
    categories: ['Для дома'] as Category[],
    expectedProducts: [products[1]],
  },
];

describe('test applyCategories function', () => {
  test.each(testCases)('should return $expectedProducts', ({ products, categories, expectedProducts}) => {
    expect(applyCategories(products, categories)).toEqual(expectedProducts);
  });
});