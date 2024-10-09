import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {

    const fixedDate = new Date('2023-10-08T12:00:00');

    beforeAll(() => {
        jest.useFakeTimers(); // Включаем фейковые таймеры для контроля времени
        jest.setSystemTime(fixedDate);
    });

    afterEach(() => {
        jest.resetAllMocks(); // Сбрасываем все моки после каждого теста
    });

    afterAll(() => {
        jest.useRealTimers(); // Возвращаем настоящие таймеры после тестов
        jest.setSystemTime(new Date());
    });

    it('должен возвращать текущее время при первом рендере', () => {
        const { result } = renderHook(() => useCurrentTime());

        // Получаем текущее время для проверки
        const currentTime = new Date().toLocaleTimeString('ru-RU');

        expect(result.current).toBe(currentTime);
    });

    it('должен обновлять время каждую секунду', () => {
        const { result } = renderHook(() => useCurrentTime());

        // Получаем текущее время для первого вызова
        const initialTime = result.current;

        // Прокручиваем таймер на 1 секунду
        act(() => {
            jest.advanceTimersByTime(1000);
        });

        // Проверяем, что текущее время изменилось через 1 секунду
        expect(result.current).not.toBe(initialTime);
        const newTime = new Date().toLocaleTimeString('ru-RU');
        expect(result.current).toBe(newTime);
    });

    it('должен очищать интервал при размонтировании', () => {
        const clearIntervalSpy = jest.spyOn(global, 'clearInterval');

        const { unmount } = renderHook(() => useCurrentTime());

        // Размонтируем хук
        unmount();

        // Проверяем, что clearInterval был вызван при размонтировании
        expect(clearIntervalSpy).toHaveBeenCalled();
    });
});
