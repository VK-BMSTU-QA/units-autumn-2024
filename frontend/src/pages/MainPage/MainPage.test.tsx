import { fireEvent, render } from '@testing-library/react';
import { MainPage } from './MainPage';
import React from 'react';
import { Category, Product } from '../../types';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';

const products: Product[] = [
    {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/iphone.png',
    },
];

const emptyCategories: Category[] = [];

jest.mock('../../utils/getPrice', () => ({
    __esModule: true,
    getPrice: jest.fn(() => ''),
}));

jest.mock('../../utils/applyCategories', () => ({
    __esModule: true,
    applyCategories: jest.fn(() => {
        return products;
    }),
}));

jest.mock('../../utils/updateCategories', () => ({
    __esModule: true,
    updateCategories: jest.fn(() => {
        return emptyCategories;
    }),
}));

jest.mock('../../hooks/useProducts', () => ({
    __esModule: true,
    useProducts: jest.fn(() => {
        return products;
    }),
}));

jest.mock('../../hooks/useCurrentTime');

afterEach(jest.clearAllMocks);
describe('Categories test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when page render', () => {
        render(<MainPage />);
        expect(useProducts).toHaveBeenCalledTimes(1);
        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(applyCategories).toHaveBeenCalledWith(products, emptyCategories);
        expect(updateCategories).toHaveBeenCalledTimes(0);
    });

    it('should update categories state after click', () => {
        const rendered = render(<MainPage />);
        fireEvent.click(rendered.getByText('Одежда'));
        expect(updateCategories).toHaveBeenCalledWith(
            emptyCategories,
            'Одежда'
        );
    });
});