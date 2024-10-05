import {fireEvent, render} from '@testing-library/react';
import { MainPage } from './MainPage';
import {Category, Product} from "../../types";
import '@testing-library/jest-dom/extend-expect';
import {useCurrentTime, useProducts} from "../../hooks";
import {applyCategories, updateCategories} from "../../utils";
import {Categories} from "../../components";

afterEach(jest.clearAllMocks);
jest.mock('../../hooks');
jest.mock('../../utils');
jest.mock('../../components/Categories');


describe("test main page", () => {
    beforeEach(() => {
        const product: Product[] = [{
            id: 3,
            name: 'Настольная лампа',
            description: 'Говорят, что ее использовали в pixar',
            price: 699,
            category: 'Для дома',
            imgUrl: '/lamp.png',
        },{
            id: 4,
            name: 'Принтер',
            description: 'Незаменимая вещь для студента',
            price: 7000,
            category: 'Электроника',
        }];
        const productsMock = product
        const timeMock = '12:00:00';
        const testCategory: Category = 'Одежда';
        const buttonText = 'button';
        const updateCategoriesMockValue = [testCategory];
        jest.mocked(useCurrentTime).mockReturnValue(timeMock);
        jest.mocked(useProducts).mockReturnValue(productsMock)
        jest.mocked(applyCategories).mockReturnValue(productsMock);
        jest.mocked(updateCategories).mockReturnValue(updateCategoriesMockValue);
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
    });
    it('should render correctly', () => {
        const rendered = render(<MainPage/>);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render products and text', () => {
        const rendered = render(<MainPage/>);
        expect(rendered.getByText('Настольная лампа')).toBeInTheDocument();
        expect(rendered.getByText('Принтер')).toBeInTheDocument();
        expect(rendered.getByText('VK Маркет')).toBeInTheDocument();
    });

    it("should change category", ()=>{
        const testCategory: Category = 'Одежда';
        const buttonText = 'button';
        const rendered = render(<MainPage />);
        fireEvent.click(rendered.getByText(buttonText));

        expect(updateCategories).toBeCalledWith([], testCategory);
        expect(rendered.getByText(testCategory)).not.toBeNull();
    })
})
