export function Button({ label = "Run", disabled = false }) {
  return (
    <button type="button" disabled={disabled}>
      {label}
    </button>
  );
}
