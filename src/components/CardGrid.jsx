import React from "react";

function CardGrid({
  title,
  data,
  renderItem,
  emptyMessage = "No data available.",
  className = "",
}) {
  return (
    <section className={`cardgrid-section ${className}`}>
      {title && <h2>{title}</h2>}

      <div className="reports-grid">
        {data.length === 0 ? (
          <p>{emptyMessage}</p>
        ) : (
          data.map((item, index) => (
            <div key={item.id || index} className="report-card">
              {renderItem(item)}
            </div>
          ))
        )}
      </div>
    </section>
  );
}

export default CardGrid;