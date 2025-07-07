import { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function ReminderList() {
  const [userId, setUserId] = useState("");
  const [reminders, setReminders] = useState([]);

  const fetchReminders = async () => {
    if (!userId.trim()) {
      toast.error("🚫 Please enter your User ID.");
      return;
    }

    try {
      const res = await axios.get("http://127.0.0.1:8000/reminders/", {
        params: { user_id: userId },
      });
      setReminders(res.data);

      if (res.data.length === 0) {
        toast.info("🔔 No reminders found for this user.");
      } else {
        toast.success(`🔍 Found ${res.data.length} reminder(s)!`);
      }
    } catch (err) {
      console.error(err);
      toast.error("❌ Failed to fetch reminders.");
    }
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow-md max-w-xl mx-auto mt-6">
      <h2 className="text-2xl font-semibold mb-4 text-[#3B5BA5]">Reminder History</h2>

      <div className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Enter your user ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-[#3B5BA5]"
        />
        <button
          onClick={fetchReminders}
          className="bg-[#3B5BA5] text-white px-4 py-2 rounded hover:bg-[#2d478c] transition"
        >
          View
        </button>
      </div>

      <ul className="space-y-2">
        {reminders.map((r) => (
          <li
            key={r.id}
            className="p-3 border rounded-md bg-[#F9F9FF] text-sm flex justify-between items-center"
          >
            <span>
              💊 <strong>{r.medicine_name}</strong> at <code>{r.time}</code>
            </span>
            <span className="text-xs text-gray-500">ID: {r.id}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReminderList;
