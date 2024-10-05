import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

jest.mock('../../utils/getPrice', () => ({
    __esModule: true,
    getPrice: jest.fn(() => '999 $'),
}));

const product: Product = {
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
};

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard key={product.id} {...product} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call callback when render', () => {
        render(<ProductCard key={product.id} {...product} />);
        expect(getPrice).toHaveBeenCalledTimes(1);
    });
});