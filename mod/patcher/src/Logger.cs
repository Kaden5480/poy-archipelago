using System;
using System.Runtime.CompilerServices;

namespace PoYArchipelagoPatcher {
    public enum LogLevel {
        NONE,
        ERROR,
        INFO,
        DEBUG,
    }

    public static class Logger {
// Don't warn about unreachable code, the level
// is hard coded and sometimes it will intentionally cause
// unreachable code
#pragma warning disable 0162

#if DEBUG
        private const LogLevel level = LogLevel.DEBUG;
#else
        private const LogLevel level = LogLevel.ERROR;
#endif

        /**
         * <summary>
         * Logs a message.
         * </summary>
         * <param name="level">The log level</param>
         * <param name="message">The message to log</param>
         * <param name="caller">The caller</param>
         */
        private static void Log(string level, string message, string caller) {
            if (Logger.level == LogLevel.NONE) {
                return;
            }

            Console.WriteLine($"[{level} : PoYArchipelagoPatcher] [{caller}] {message}");
        }

        /**
         * <summary>
         * Logs a debug message.
         * </summary>
         * <param name="message">The message to log</param>
         * <param name="caller">The caller</param>
         */
        public static void LogDebug(string message, [CallerMemberName] string caller = "") {
            if (level < LogLevel.DEBUG) {
                return;
            }

            Log("Debug ", message, caller);
        }

        /**
         * <summary>
         * Logs an informational message.
         * </summary>
         * <param name="message">The message to log</param>
         * <param name="caller">The caller</param>
         */
        public static void LogInfo(string message, [CallerMemberName] string caller = "") {
            if (level < LogLevel.INFO) {
                return;
            }

            Log("Info  ", message, caller);
        }

        /**
         * <summary>
         * Logs an error message.
         * </summary>
         * <param name="message">The message to log</param>
         * <param name="caller">The caller</param>
         */
        public static void LogError(string message, [CallerMemberName] string caller = "") {
            if (level < LogLevel.ERROR) {
                return;
            }

            Log("Error ", message, caller);
        }

#pragma warning restore 0162

    }
}
