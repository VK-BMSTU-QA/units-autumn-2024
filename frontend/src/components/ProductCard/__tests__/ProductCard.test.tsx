import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from '../ProductCard';
import { getPrice } from '../../../utils';

afterEach(jest.clearAllMocks);
jest.mock('../../../utils');

describe('ProductCard component tests', () => {
    it('should mock getPrice function and display correct formatted price', () => {
        jest.mocked(getPrice).mockReturnValue('200 $');

        const rendered = render(
            <ProductCard
                id={101}
                name={'Samsung Galaxy S21'}
                description={'Latest Samsung smartphone'}
                price={200}
                category={'Электроника'}
                priceSymbol={'$'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(getPrice).toHaveBeenCalledWith(200, '$');
        expect(getPrice).lastReturnedWith('200 $');
    });

    it('should render the product image with given URL', () => {
        const rendered = render(
            <ProductCard
                id={102}
                name={'Dell XPS 13'}
                description={'Ultra-slim laptop'}
                price={1500}
                category={'Электроника'}
                imgUrl={'public/dell-xps.png'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.getByAltText('Dell XPS 13')).toHaveClass(
            'product-card__image'
        );
    });

    it('should not render image if imgUrl is not provided', () => {
        const rendered = render(
            <ProductCard
                id={103}
                name={'Sony WH-1000XM4'}
                description={'Noise-cancelling headphones'}
                price={300}
                priceSymbol={'$'}
                category={'Электроника'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.queryAllByAltText('Sony WH-1000XM4')).toHaveLength(0);
        expect(rendered.queryByAltText('Sony WH-1000XM4')).not.toBeInTheDocument();
    });

});
