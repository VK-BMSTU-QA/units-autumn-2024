import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import { ProductCard } from './ProductCard';
import { useProducts } from '../../hooks';
import { getPrice } from '../../utils';

jest.mock('../../utils');

const products = useProducts();

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard {...products[1]} />);

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should contain properties', () => {
        const rendered = render(<ProductCard {...products[1]} />);

        expect(getPrice).toHaveBeenCalledTimes(2);

        expect(rendered.getByText('Костюм гуся')).toBeInTheDocument();
        expect(rendered.getByText('Запускаем гуся, работяги')).toHaveClass(
            'product-card__description'
        );
        expect(rendered.getByText('Одежда')).toHaveClass(
            'product-card__category'
        );
    });
});
