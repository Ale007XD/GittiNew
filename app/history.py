import aiosqlite

DB_PATH = "history.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS history (
            user_id INTEGER,
            message TEXT,
            role TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        await db.commit()

async def get_history(user_id: int, limit: int = 10):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT message, role FROM history WHERE user_id=? ORDER BY timestamp DESC LIMIT ?", (user_id, limit)
        )
        rows = await cursor.fetchall()
        # Формируем [{"role": ..., "message": ...}, ...], свежие — внизу
        return [{"role": r[1], "message": r[0]} for r in reversed(rows)]

async def add_message(user_id: int, message: str, role: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO history (user_id, message, role) VALUES (?, ?, ?)", (user_id, message, role)
        )
        await db.commit()

