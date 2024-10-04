import React, { useEffect, useState } from 'react';
import { MainPage } from './MainPage';
import { fireEvent, render } from '@testing-library/react';
import { useCurrentTime, useProducts } from '../../hooks';
import { Category, Product } from '../../types';
import { applyCategories, updateCategories } from '../../utils';
import { Categories } from '../../components';

afterEach(jest.clearAllMocks);
jest.mock('../../hooks');
jest.mock('../../utils');
jest.mock('../../components/Categories');

describe('MainPage test', () => {
    it('should render correctly', () => {
        const product: Product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        };
        const productsMockValue = [product];
        const timeMockValue = '12:00:00';
        jest.mocked(useProducts).mockReturnValue(productsMockValue);
        jest.mocked(useCurrentTime).mockReturnValue(timeMockValue);
        jest.mocked(applyCategories).mockReturnValue(productsMockValue);
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(useProducts).toBeCalledTimes(1);
        expect(useCurrentTime).toBeCalledTimes(1);
        expect(applyCategories).toBeCalledTimes(1);
    });
    it('should change list of categories when onCategoryClick is called', () => {
        const testCategory: Category = 'Одежда';
        const buttonText = 'button';
        const updateCategoriesMockValue = [testCategory];
        jest.mocked(updateCategories).mockReturnValue(
            updateCategoriesMockValue
        );
        jest.mocked(Categories).mockImplementation(
            ({ selectedCategories, onCategoryClick }) => (
                <div>
                    <button onClick={() => onCategoryClick?.(testCategory)}>
                        {buttonText}
                    </button>
                    {selectedCategories.map((category) => (
                        <p key={category}>{category}</p>
                    ))}
                </div>
            )
        );

        const rendered = render(<MainPage />);
        fireEvent.click(rendered.getByText(buttonText));

        expect(updateCategories).toBeCalledWith([], testCategory);
        expect(rendered.getByText(testCategory)).not.toBeNull();
    });
});
