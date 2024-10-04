import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {
    beforeAll(() => {
        jest.useFakeTimers(); // Включаем фейковые таймеры для контроля времени
    });

    afterAll(() => {
        jest.useRealTimers(); // Возвращаем настоящие таймеры после тестов
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
