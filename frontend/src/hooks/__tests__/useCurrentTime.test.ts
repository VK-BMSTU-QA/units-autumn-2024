import { renderHook, act } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

jest.useFakeTimers();

describe('useCurrentTime hook', () => {
    it('should return current time', () => {
        const { result } = renderHook(() => useCurrentTime());
        const currentTime = result.current;

        expect(currentTime).toEqual(expect.any(String));

        // Мокуем таймер, чтобы проверить, обновляется ли время через 1 секунду
        act(() => {
            jest.advanceTimersByTime(1000); // Ускоряем время на 1 секунду
        });

        const updatedTime = result.current;
        expect(updatedTime).toEqual(expect.any(String));
        expect(updatedTime).not.toEqual(currentTime); // Ожидаем обновления времени
    });
});
