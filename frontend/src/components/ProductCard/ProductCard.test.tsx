import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

jest.mock('../../utils');

const ProductCardd = (overrides = {}) => (
    <ProductCard
        id={1}
        name="Really Good Name"
        description="Good Description"
        price={12764}
        category="Одежда"
        {...overrides}
    />
);

describe('test ProductCard', () => {
    it('should render', () => {
        const rendered = render(ProductCardd({ imgUrl: '/lamp.png' }));

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call getPrice', () => {
        render(ProductCardd());

        expect(getPrice).toHaveBeenCalledWith(12764, undefined);
    });

    it('should get price from getPrice', () => {
        jest.mocked(getPrice).mockReturnValue('42142 ₽');

        const rendered = render(ProductCardd());

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should not render img', () => {
        const rendered = render(ProductCardd());

        expect(rendered.queryByRole('img')).toBeNull();
    });
});