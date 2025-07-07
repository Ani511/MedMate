import { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";

function ReminderForm() {
  const [formData, setFormData] = useState({
    user_id: "",
    email: "",
    medicine_name: "",
    time: "",
  });

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:8000/reminders/", formData);
      toast.success("🎉 Reminder set! MedMate won’t forget it!");
      setFormData({
        user_id: "",
        email: "",
        medicine_name: "",
        time: "",
      });
    } catch (error) {
      console.error(error);
      toast.error("😕 Failed to add reminder.");
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="p-4 bg-white rounded-lg shadow-md max-w-xl mx-auto my-4"
    >
      <h2 className="text-2xl font-semibold mb-4 text-[#009999]">Schedule My Dose</h2>

      <div className="mb-3">
        <label className="block mb-1 font-medium">User ID</label>
        <input
          name="user_id"
          value={formData.user_id}
          onChange={handleChange}
          className="w-full p-2 border rounded-md"
          required
        />
      </div>

      <div className="mb-3">
        <label className="block mb-1 font-medium">Email</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          className="w-full p-2 border rounded-md"
          required
        />
      </div>

      <div className="mb-3">
        <label className="block mb-1 font-medium">Medicine Name</label>
        <input
          name="medicine_name"
          value={formData.medicine_name}
          onChange={handleChange}
          className="w-full p-2 border rounded-md"
          required
        />
      </div>

      <div className="mb-3">
        <label className="block mb-1 font-medium">Time (HH:MM)</label>
        <input
          type="time"
          name="time"
          value={formData.time}
          onChange={handleChange}
          className="w-full p-2 border rounded-md"
          required
        />
      </div>

      <button
        type="submit"
        className="bg-[#009999] text-white px-4 py-2 rounded hover:bg-[#007777] transition"
      >
        Add Reminder
      </button>
    </form>
  );
}

export default ReminderForm;
