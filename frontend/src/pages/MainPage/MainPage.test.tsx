import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { Product, Category } from '../../types';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';
import { act } from 'react-dom/test-utils';

jest.mock('../../utils');
jest.mock('../../hooks');
jest.mock('../../components', () => ({
    __esModule: true,
    Categories: (props: {
        selectedCategories: Category[];
        onCategoryClick: (category: Category) => void;
    }) => (
        <div>
            {fixtureFilters.map((filter) => (
                <div
                    onClick={() => props.onCategoryClick?.(filter)}
                    className={props.selectedCategories.includes(filter) ? "selected" : ""}
                >
                    {filter}
                </div>
            ))}
        </div>
    ),
    ProductCard: (product: Product) => (
        <div className="product-card__text">
            <div data-id={product.id} data-name={product.name}>{product.name}</div>
            <div data-id={product.id} data-description={product.description}>{product.description}</div>
            <div data-id={product.id} data-price={product.price}>{product.price}</div>
        </div>

    ),
}));

const fixtureFilters: Category[] = ['Одежда', 'Для дома', 'Электроника'];

const fixturesProducts: Product[] = [
    {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iphone, buy it now',
        price: 999,
        category: 'Электроника',
    },
    {
        id: 2,
        name: 'Костюм гуся',
        description: 'Запускаем гуся, работяги',
        price: 1000,
        category: 'Одежда',
    },
    {
        id: 3,
        name: 'Настольная лампа',
        description: 'Говорят, что ее использовали в pixar',
        price: 699,
        category: 'Для дома',
    },
    {
        id: 4,
        name: 'Принтер',
        description: 'Незаменимая вещь для студента',
        price: 7000,
        category: 'Электроника',
    },
];

afterEach(jest.clearAllMocks);
describe('MainPage test', () => {
    beforeEach(() => {
        jest.mocked(applyCategories).mockReturnValue(fixturesProducts);
        jest.mocked(useCurrentTime).mockReturnValue('time');
    });

    it('should be displayed correctly', () => {
        const rendered = render(<MainPage/>);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should select category', () => {
        jest.mocked(updateCategories).mockReturnValue(['Одежда']);

        const rendered = render(<MainPage/>);

        act(() => fireEvent.click(rendered.getByText('Одежда')));

        expect(applyCategories).toHaveBeenCalledTimes(2);
        expect(updateCategories).toHaveBeenCalledTimes(1);

        expect(rendered.getByText('Одежда')).toHaveClass('selected');
        expect(rendered.getByText('Электроника')).not.toHaveClass('selected');
        expect(rendered.getByText('Для дома')).not.toHaveClass('selected');
    });

    it('should display products', () => {
        const rendered = render(<MainPage/>);

        expect(applyCategories).toHaveBeenCalledTimes(1);
        expect(rendered.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(rendered.getByText('Костюм гуся')).toBeInTheDocument();
        expect(rendered.getByText('Настольная лампа')).toBeInTheDocument();
        expect(rendered.getByText('Принтер')).toBeInTheDocument();
    });

    it('should select few categories', () => {
        jest.mocked(updateCategories)
            .mockReturnValueOnce(['Одежда'])
            .mockReturnValueOnce(['Одежда', 'Электроника']);

        const rendered = render(<MainPage/>);

        act(() => fireEvent.click(rendered.getByText('Одежда')));
        act(() => fireEvent.click(rendered.getByText('Электроника')));

        expect(applyCategories).toHaveBeenCalledTimes(3);
        expect(updateCategories).toHaveBeenCalledTimes(2);

        expect(rendered.getByText('Одежда')).toHaveClass('selected');
        expect(rendered.getByText('Электроника')).toHaveClass('selected');
        expect(rendered.getByText('Для дома')).not.toHaveClass('selected');
    });

    it('should select all categories', () => {
        jest.mocked(updateCategories)
            .mockReturnValueOnce(['Одежда'])
            .mockReturnValueOnce(['Одежда', 'Электроника'])
            .mockReturnValueOnce(['Одежда', 'Электроника', 'Для дома']);

        const rendered = render(<MainPage/>);

        act(() => fireEvent.click(rendered.getByText('Одежда')));
        act(() => fireEvent.click(rendered.getByText('Электроника')));
        act(() => fireEvent.click(rendered.getByText('Для дома')));

        expect(applyCategories).toHaveBeenCalledTimes(4);
        expect(updateCategories).toHaveBeenCalledTimes(3);

        expect(rendered.getByText('Одежда')).toHaveClass('selected');
        expect(rendered.getByText('Электроника')).toHaveClass('selected');
        expect(rendered.getByText('Для дома')).toHaveClass('selected');
    });

    it('should be render time', () => {
        const rendered = render(<MainPage/>);

        expect(useCurrentTime).toHaveBeenCalledTimes(1);
        expect(rendered.getByText('time')).toBeInTheDocument();
    });
});