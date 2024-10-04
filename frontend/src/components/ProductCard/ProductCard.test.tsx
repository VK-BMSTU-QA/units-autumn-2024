import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

jest.mock('../../utils');

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(
            <ProductCard
                id={1}
                name={'name'}
                description={'desc'}
                price={100}
                category={'Одежда'}
                imgUrl={'/lamp.png'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call getPrice', () => {
        render(
            <ProductCard
                id={1}
                name={'name'}
                description={'desc'}
                price={100}
                category={'Одежда'}
            />
        );

        expect(getPrice).toHaveBeenCalledWith(100, undefined);
    });

    it('should get price from getPrice', () => {
        jest.mocked(getPrice).mockReturnValue('100 bubbles');

        const rendered = render(
            <ProductCard
                id={1}
                name={'name'}
                description={'desc'}
                price={100}
                category={'Одежда'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should not render img', () => {
        const rendered = render(
            <ProductCard
                id={1}
                name={'name'}
                description={'desc'}
                price={100}
                category={'Одежда'}
            />
        );

        expect(rendered.queryByRole('img')).toBeNull();
    });
});
