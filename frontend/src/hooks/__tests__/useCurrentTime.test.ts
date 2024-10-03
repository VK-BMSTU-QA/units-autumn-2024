// useCurrentTime.test.js

import { renderHook, act } from '@testing-library/react-hooks';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime', () => {
  beforeEach(() => {
    jest.useFakeTimers(); // Переместили внутрь beforeEach
  });

  afterEach(() => {
    jest.clearAllTimers();
    jest.useRealTimers(); // Возвращаем реальные таймеры после каждого теста
  });

  test('возвращает текущее время и обновляется каждую секунду', () => {
    const { result } = renderHook(() => useCurrentTime());

    const initialTime = result.current;

    // Проматываем время на 1 секунду
    act(() => {
      jest.advanceTimersByTime(1000);
    });

    expect(result.current).not.toBe(initialTime);
  });

  test('очищает интервал при размонтировании', () => {
    const { unmount } = renderHook(() => useCurrentTime());

    expect(jest.getTimerCount()).toBe(1); // Убедимся, что таймер установлен

    unmount();

    expect(jest.getTimerCount()).toBe(0); // Проверяем, что таймер очищен
  });
});
